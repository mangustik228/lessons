FROM node:18.13.0-alpine 

WORKDIR /app 
COPY ./package.json . 
RUN npm install
# CMD [ "npm", "run", "serv" ]
CMD [ "npm", "run", "dev" ]
