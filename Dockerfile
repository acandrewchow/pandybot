FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Run deploy commands
RUN node src/deploy-commands.js

# Set the default command to start your application
CMD ["node", "./src/index.js"]
