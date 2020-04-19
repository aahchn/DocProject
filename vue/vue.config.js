// vue.config.js - fix CORS problem
// https://www.youtube.com/watch?v=WsYrDu7xkEw
module.exports = {
  devServer: {
    proxy: 'http://localhost:5000'
  }
};
