const express = require('express');
const bodyParser = require('body-parser');
const TelegramBot = require('node-telegram-bot-api');

const app = express();
app.use(bodyParser.json());

const bot = new TelegramBot('YOUR_BOT_TOKEN', { polling: true });

bot.onText(/\/upload (.+)/, (msg, match) => {
  const url = match[1];
  const chatId = msg.chat.id;

  // Upload URL to Render or Koyeb instance
  const renderUrl = `https://your-render-instance.com/upload?url=${url}`;
  const koyebUrl = `https://your-koyeb-instance.com/upload?url=${url}`;

  // Send uploaded file to Telegram chat
  bot.sendDocument(chatId, renderUrl || koyebUrl);
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
