FROM node:9.5

# Specify the version so builds are (more) reproducible.
RUN npm install --quiet --global vue-cli@2.9.3

RUN mkdir /app
WORKDIR /app