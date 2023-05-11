var axios = require("axios");
var qs = require("qs");

let username = "1rl37q3fah8aaacvru1lnrmnf";
let password = "1srkk5ohfheta3ssmq0rbqqnb9c7fckt7e8hip03400qh0t4da7i";
let auth = Buffer.from(`${username}:${password}`).toString("base64");


const login = async () => {
  try {
    const ArchitecturePath = "https://developer.konfio.mx/api/techdocs/static/docs/default/resource/wiki/index.html"
    var response = await axios.get(ArchitecturePath);
    console.log(response.data)
    return response.text;
  } catch (error) {
    const { status, message, config } = console.error(error);
    throw new Error(`${error.message} & code: ${error.response.data.code}`);
  }
};
const start = async () =>{
    try{
       let data = await login()
       console.log(data)
    }catch (error){
        console.error(error.message)
    }
}
start()