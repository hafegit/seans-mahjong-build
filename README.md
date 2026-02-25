# Sean's Project Experiments

A collection of HTML game projects and web experiments.

## 🎮 Current Projects

### Mahjong Game
An interactive HTML-based Mahjong game featuring custom artwork.

**[Play the game here](https://hafegit.github.io/seans-mahjong-build/mahjong-game/)**

#### Features
- Custom tile designs with latte art and pet images
- Pure HTML/CSS/JavaScript implementation
- Playable directly in the browser
- **Progressive Web App (PWA)** - Install as a native app on your phone!

---

## 📱 Install as an App (Android & iOS)

You can install this game as a full-screen app on your phone - no app store needed!

### 🤖 Android Installation

1. **Open the game** in Chrome on your Android phone:
   - Visit: <https://hafegit.github.io/seans-mahjong-build/mahjong-game/>

2. **Install the app**:
   - Chrome will show a banner at the bottom: **"Add Mahjong to Home Screen"**
   - Tap the banner to install
   
3. **Launch the game**:
   - Find the gold Mahjong tile icon on your home screen
   - Tap to launch - it opens full-screen like a native app!
   - No browser chrome, no URL bar - just the game

### 🍎 iOS Installation

1. **Open the game** in Safari on your iPhone:
   - Visit: <https://hafegit.github.io/seans-mahjong-build/mahjong-game/>

2. **Add to Home Screen**:
   - Tap the **Share** button (square with arrow pointing up)
   - Scroll down and tap **"Add to Home Screen"**
   - Tap **"Add"** in the top right

3. **Launch the game**:
   - Find the gold Mahjong tile icon on your home screen
   - Tap to launch - it opens full-screen!

### ✨ Benefits of Installing as an App
- **Full-screen experience** - No browser UI cluttering the game
- **Quick access** - Launch from your home screen like any other app
- **Works offline** - Play even without an internet connection (after first load)
- **Faster loading** - Assets are cached for instant startup

---

## 💻 Play in Browser

Don't want to install? No problem! Just visit the link and play directly in any modern web browser:
- **Desktop**: Chrome, Firefox, Safari, Edge
- **Mobile**: Any mobile browser

---

## 📁 Repository Structure

```
seans-mahjong-build/
├── mahjong-game/
│   ├── index.html          # Main game file
│   ├── manifest.json       # PWA configuration
│   ├── sw.js              # Service worker for offline support
│   ├── icons/             # App icons (192x192, 512x512)
│   ├── images/            # Game tile images
│   │   ├── latte/         # Latte art tiles
│   │   └── pets/          # Pet tiles
│   └── make_icons.py      # Icon generator script
└── README.md
```

---

## 🚀 Getting Started (Local Development)

To run the game locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/hafegit/seans-mahjong-build.git
   ```

2. Navigate to the game folder:
   ```bash
   cd seans-mahjong-build/mahjong-game
   ```

3. Open `index.html` in your web browser

---

## 🔄 For Developers: Updating the PWA

When you push updates to the game, **remember to update the cache version** in `sw.js`:

```javascript
// Change this line in sw.js:
const CACHE_NAME = 'pmj-pwa-v1';  // Increment to v2, v3, etc.
```

This forces all installed apps to fetch fresh assets on next launch.

---

## 📝 Future Projects

This repository is designed to be flexible for additional game projects and experiments. Stay tuned for more!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

This is a personal project repository, but feel free to fork and experiment with your own versions!
