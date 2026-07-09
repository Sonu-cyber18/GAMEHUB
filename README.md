# 🎮 Django Arcade Central & 3D Game Platform

Welcome to the **Django Arcade Central**, a premium web-based retro arcade housing classic grid games alongside advanced 3D WebGL (Three.js) sandbox and strategy experiences. Powered by a Django backend with full user accounts, settings, and leaders dashboards.

---

## 🚀 Featured Games

### 🎯 1. Stickman Hitman 3D (Stealth Strategy)
A premium 3D WebGL infiltration game built with Three.js. You play as Agent 47, tasked with completing strategic contracts.
* **Stealth Mechanics**: Evade orange guards and their translucent visual Line-of-Sight vision cones. Entering cones rises suspicion telemetry.
* **Weapon Loadout**: Swap weapons on-the-fly (`1` for Knife, `2` for Pistol, `3` for Sniper). Sound sensors alert guards based on gunshot radius.
* **Tactical Scope**: Click Right-Click or `Shift` with the Sniper to trigger a 18° FOV zoomed scope crosshair overlay.
* **Tactical Circular Radar**: A glassmorphic minimap HUD scanning beacons of nearby guards and contract targets.

### 🚗 2. ITF - Grand Theft Stickman 3D
A 3D open-world city sandbox featuring vehicle driving and police chaser AI.
* **Drive & Explore**: Hop in cars, speed down streets, and steer with physics-based kinematics.
* **Wanted Stars & Sirens**: Accumulating wanted levels triggers police squad dispatch chasing you down with flashing light sirens.

### 🐍 3. Retro Classics Catalog
* **Neon Rush (Hill Climber)**: Physics-based vehicle driving over high-speed neon hills with leaderboard score saving.
* **Snake**: Custom grid speed controls and high score metrics.
* **Chess**: Complete chess engine with board configurations for local matches.
* **Pacman**: Maze-runner navigation with active ghost path AI.
* **Ludo, Flappy Bird, Memory Match, and Python Learning Game**.

---

## 🛠️ Tech Stack
* **Backend**: Django (Python) handles authentication, routing, and user dashboard profiles.
* **3D Graphics**: Three.js (WebGL) rendering meshes, lights, shadows, and vision cones.
* **2D Graphics**: HTML5 Canvas overlays mapping circular radars, scopes, and minimaps.
* **Sound Engine**: Web Audio API synthesizing custom pistol cracks, sniper fire blasts, alarms, and engine rev sounds.

---

## 💻 Quick Start & Setup

### Prerequisites
* Python 3.10+
* Django 4.x

### Run Django Locally
1. **Clone the repository**:
   ```bash
   cd snake_game
   ```
2. **Install dependencies**:
   ```bash
   pip install django
   ```
3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
4. **Launch development server**:
   ```bash
   python manage.py runserver 8000
   ```
5. **Access the portal**: Open `http://127.0.0.1:8000/` in your browser. Register an account to explore the dashboard card selections.

---

## 🎮 Platform Controls Map

| Input | Action |
| :--- | :--- |
| **`W` / `A` / `S` / `D` or Arrows** | Character / Vehicle Movement |
| **Mouse Drag / Swipe** | Camera Orbit Rotation |
| **`1` / `2` / `3` keys** | Select Weapon (Knife / Pistol / Sniper) |
| **`Shift` or Right-Click** | Toggle Sniper Scope Zoom |
| **Left-Click** | Attack / Fire Bullet / Interact |
| **`Space`** | Handbrake / Brake (ITF driving) |
| **`F` / `Enter`** | Enter / Exit Vehicle (ITF driving) |
