const { REST } = require("discord.js");
const { Routes } = require("discord-api-types/v9");
const { TOKEN, CLIENT_ID } = require("../config/config.js");

const rest = new REST({ version: "10" }).setToken(TOKEN);

const registerCommands = async (commands) => {
    try {
        console.log("Started refreshing application (/) commands.");
        await rest.put(Routes.applicationCommands(CLIENT_ID), { body: commands });
        console.log("Successfully reloaded application (/) commands.");
    } catch (error) {
        console.error(error);
    }
};

module.exports = registerCommands;
