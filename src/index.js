const {Client, GatewayIntentBits, EmbedBuilder, PermissionsBitField, Permissions} = require('discord.js')

const client = new Client({intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent]})
const { token } = require('./config/config.js');


client.on("ready", () => {
    console.log("Bot is online!")
})



client.login(token)