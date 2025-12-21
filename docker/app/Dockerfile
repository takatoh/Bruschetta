FROM node:24 AS builder

RUN git clone https://github.com/takatoh/bruschetta.git

WORKDIR /bruschetta/app
COPY files/.env.prod .
RUN npm install
RUN npm run build


FROM nginx:1.29.3

COPY --from=builder /bruschetta/app/dist/spa/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
