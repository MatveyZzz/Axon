🧠 Axon — AI-powered Telegram Bot for Scientific Research
Axon is an intelligent Telegram bot that helps you find and explore scientific research on any topic — from biotechnology and AI to physics and environmental science.

🚀 Project Status

✅ Telegram bot core framework implemented
✅ Topic-based search powered by a local JSON knowledge base
✅ Initial dataset of scientific papers and insights created
🧩 Ready for integration with APIs, AI models, and advanced analytics

🧠 Features

🔍 Search for scientific research by keywords or topics

🧬 Browse curated insights from open scientific databases

💡 Simple JSON-based architecture for rapid prototyping

🤖 Built on python-telegram-bot for stability and async performance

🧩 Tech Stack
Component	Description
Language	Python 3.10+
Framework	python-telegram-bot
Data Storage	JSON (local file)
Async Runtime	asyncio
Planned	OpenAI / DeepSeek API integration
⚙️ Installation

Clone the repository

git clone https://github.com/<your_username>/axon-bot.git
cd axon-bot


Install dependencies

pip install -r requirements.txt


Create configuration file
Create a file named config.py in the project root and add your Telegram API token:

telegram_bot_api = "YOUR_TELEGRAM_API_TOKEN"


Run the bot

python main.py

💬 Example Interaction
/start
> Hi! I'm Axon — your guide through the world of science and innovation.
> Type a topic (e.g. "biotech" or "AI in medicine") to find research insights.

AI in medicine
> 🔬 Using Artificial Intelligence in Radiology
> 💡 New algorithms increase diagnostic accuracy by 35%.
> 🚀 Application: Medical startups, diagnostics, image analysis.
> Source: https://doi.org/10.xxxxx/xxxxx

⚠️ Security Note

The file config.py is not included in this repository because it contains private tokens for Telegram API access.
You must create your own config.py locally as described above.

🧭 Roadmap

🤖 Integration with OpenAI / DeepSeek for smart summaries

📚 Expansion of the research database (1,000+ entries planned)

🔍 Advanced multi-keyword search

📰 Scientific news aggregator

🌐 Multilingual interface (RU / EN)

🧑‍💻 Author

Axon is a personal learning and research project built in Russia by a young developer passionate about science and technology.

📬 Contact via Telegram

📜 License

This project is released under the MIT License — feel free to use, modify, and contribute.
