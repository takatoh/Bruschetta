FROM node:24

# node:24 のイメージには、`node` という uid=1000、
# gid=1000 のユーザがあらかじめ存在する。

WORKDIR /app
USER node

#RUN npm install

CMD ["npm", "run", "dev"]
