FROM node:9.11.1-alpine
WORKDIR /www/frontend

COPY package.json .
RUN npm install --quiet
EXPOSE 3000
COPY . .