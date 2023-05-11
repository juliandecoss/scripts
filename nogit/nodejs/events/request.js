var axios = require("axios");
var qs = require("qs");

let username = "1rl37q3fah8aaacvru1lnrmnf";
let password = "1srkk5ohfheta3ssmq0rbqqnb9c7fckt7e8hip03400qh0t4da7i";
let auth = Buffer.from(`${username}:${password}`).toString("base64");


const login = async () => {
  headers = {
    Authorization: `Basic ${auth}`,
    "Content-Type": "application/x-www-form-urlencoded",
  };
  var data = qs.stringify({
    grant_type: "client_credentials",
    clientId: "mh7m45lopkh30ipqbtfmvg0r",
  });
  try {
    var response = await axios.post("https://dev-sso.konfio.mx/token", data, {
      headers: headers,
    });
    console.log(response.data)
    return response.data;
  } catch (error) {
    const { status, message, config } = console.error(error);
    throw new Error(`${error.message} & code: ${error.response.data.code}`);
  }
};
const start = async () =>{
    try{
       let data = await login()
       console.log(data.accessToken)
    }catch (error){
        console.error(error.message)
    }
}
start()
