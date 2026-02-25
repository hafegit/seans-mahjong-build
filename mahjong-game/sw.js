// Service Worker — Sean's AI New Year Mahjong
// Bump CACHE_NAME whenever you deploy changes so users get fresh assets.
const CACHE_NAME = 'pmj-pwa-v1';

const PRECACHE = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  // Pet images
  './images/pets/p01.jpg',
  './images/pets/p02.jpg',
  './images/pets/p03.jpg',
  './images/pets/p04.jpg',
  './images/pets/p05.jpg',
  './images/pets/p06.jpg',
  './images/pets/p07.jpg',
  './images/pets/p08.jpg',
  './images/pets/p09.jpg',
  // Latte art images
  './images/latte/l01.jpg',
  './images/latte/l02.jpg',
  './images/latte/l03.jpg',
  './images/latte/l04.jpg',
  './images/latte/l05.jpg',
  './images/latte/l06.jpg',
  './images/latte/l07.jpg',
  './images/latte/l08.jpg',
  './images/latte/l09.jpg',
  './images/latte/l10.jpg',
  './images/latte/l11.jpg',
  './images/latte/l12.jpg',
  './images/latte/l13.jpg',
  './images/latte/l14.jpg',
];

// Pre-cache all game assets on install
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(PRECACHE))
  );
  self.skipWaiting();
});

// Remove old caches on activate
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Cache-first for pre-cached assets; network-first for everything else
self.addEventListener('fetch', e => {
  // Only handle GET requests
  if (e.request.method !== 'GET') return;

  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(response => {
        // Dynamically cache same-origin responses (e.g. Google Fonts)
        if (response.ok && e.request.url.startsWith(self.location.origin)) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(e.request, clone));
        }
        return response;
      }).catch(() => cached || new Response('Offline', { status: 503 }));
    })
  );
});
