FROM node:15.8.0

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app/
WORKDIR /home/node/app/

COPY --chown=node:node package*.json /home/node/app/
COPY --chown=node:node . /home/node/app

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
USER node
RUN npm config set prefix /home/node/.npm-global

RUN npm install vue-cli -g
RUN npm install


EXPOSE 8080

CMD ["npm", "run", "serve"]