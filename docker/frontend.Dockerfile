FROM node:18
WORKDIR /app
COPY frontend/ .
RUN npm install && npm run build
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
