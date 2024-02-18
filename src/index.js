const { TOKEN} = require("./config/config.js");
const { Client, GatewayIntentBits } = require("discord.js");
const registerCommands = require("./commands/registerCommands");
const pingCommand = require("./commands/ping");

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

const commands = [pingCommand];

// Load all commands async
(async () => {
    await registerCommands(commands);
})();

client.on("ready", () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
    if (!interaction.isCommand()) return;
    if (interaction.commandName === 'ping') {
        await interaction.reply('Pong!');
    }
});


// Login bot
client.login(TOKEN);