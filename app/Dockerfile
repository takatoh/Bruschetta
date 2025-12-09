FROM node:24 AS builder

WORKDIR /app

COPY ./ ./

RUN npm install

RUN npm run build


FROM nginx:1.29.3

COPY --from=builder /app/dist/spa/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
