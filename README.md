# 🧾 Ticky

**Ticky** is a small, lightweight Discord bot that helps you create and manage support tickets easily.  
Built with simplicity and productivity in mind.

---

## 🚀 Features

- Create and manage support tickets directly on Discord  
- Lightweight and easy to deploy  
- Uses modern Python tooling with [`uv`](https://docs.astral.sh/uv/)  
- Environment-based configuration  

---

## ⚙️ Installation

Make sure you have **Python 3.10+** and **uv** installed.

```bash
# Install uv if you don't have it yet
pip install uv
```
Then, clone the repository and install dependencies:
```bash
git clone https://github.com/Xavier-Msrt/ticky.git
cd ticky
uv install
```

## 🤖 Creating Your Discord Bot

Before running Ticky, you’ll need to create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).

1. Go to **[https://discord.com/developers/applications](https://discord.com/developers/applications)**
2. Click **“New Application”** and give it a name (for example: `Ticky`)
3. In the left sidebar, go to **“Bot”**
4. Click **“Reset Token”** to generate your bot token

   > ⚠️ Copy it immediately — you won’t be able to see it again later.
5. On the same page, enable the following **Privileged Gateway Intents**:

   * ✅ **Server Members Intent**
   * ✅ **Message Content Intent**
6. Copy the token and create a `.env` file in the project root:

   ```bash
   DISCORD_TOKEN=your_discord_bot_token_here
   ```


## 🔗 Inviting the Bot to Your Server

To invite your bot to a server:

1. Go back to your app in the **Discord Developer Portal**
2. Navigate to **OAuth2 → URL Generator**
3. Under **Scopes**, check:

   * `bot`
4. Under **Bot Permissions**, select the permissions your bot needs, for example:

   * `Send Messages`
   * `Read Message History`
   * `Manage Channels`
   * (Add others as needed)
5. Copy the generated URL at the bottom
6. Open it in your browser and select the server where you want to invite your bot

> 💡 You can adjust permissions based on what your bot does.
> Example (full admin link):
> `https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot`

---

## ▶️ Usage

Run the bot using:

```bash
uv run python main.py
```

---

## 💡 Why Ticky?

* Great for learning and experimenting with **Python + Discord API**
* Simple example of a **modular, event-driven bot**
* No heavy frameworks — just clean, maintainable code

---
