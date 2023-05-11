let env = "local";
let location = 'platform.konfio.mx/auth/login';
let logInUrls = [
    `https://${location}`,
    '/user/login',
  ];
if (env === 'local') logInUrls.shift();
console.log(logInUrls)