# Base image
FROM node:20-alpine

WORKDIR /app
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy src code
COPY . .

# Port config
EXPOSE 5173

# Start server
CMD ["npm", "run", "dev", "--", "--host"]