
// let username = "1rl37q3fah8aaacvru1lnrmnff";
// let password = "1srkk5ohfheta3ssmq0rbqqnb9c7fckt7e8hip03400qh0t4da7i";
// let auth = Buffer.from(`${username}:${password}`).toString('base64');
// let auth2 = "MXJsMzdxM2ZhaDhhYWFjdnJ1MWxucm1uZmY6MXNya2s1b2hmaGV0YTNzc21xMHJicXFuYjljN2Zja3Q3ZThoaXAwMzQwMHFoMHQ0ZGE3aQ=="
// console.log(auth)
// console.log(auth2)
// console.log(auth2 === basicAuth);

// Fields = [
//   {
//     name: "clave_sia",
//     type: "string",
//   },
//   {
//     name: "elemento_entrada_sia",
//     type: "string",
//   },
//   {
//     name: "codigo_entidad",
//     type: "string",
//   },
//   {
//     name: "tipo_mensaje",
//     type: "string",
//   },
//   {
//     name: "pan",
//     type: "string",
//   },
//   {
//     name: "cuenta",
//     type: "string",
//   },
//   {
//     name: "tipo_operacion",
//     type: "string",
//   },
//   {
//     name: "monto_transaccion",
//     type: "string",
//   },
//   {
//     name: "monto_transaccion_moneda_titular",
//     type: "string",
//   },
//   {
//     name: "fecha_hora_dispositivo_origen",
//     type: "string",
//   },
//   {
//     name: "numero_transaccion_origen",
//     type: "string",
//   },
//   {
//     name: "codigo_categoria_comercio",
//     type: "string",
//   },
//   {
//     name: "entidad_adquiriente",
//     type: "string",
//   },
//   {
//     name: "datos_punto_servicio_terminal",
//     type: "string",
//   },
//   {
//     name: "tasas",
//     type: "string",
//   },
//   {
//     name: "indentificador_adquiriente",
//     type: "string",
//   },
//   {
//     name: "numero_autorizacion",
//     type: "string",
//   },
//   {
//     name: "codigo_accion_sia",
//     type: "string",
//   },
//   {
//     name: "identificador_terminal",
//     type: "string",
//   },
//   {
//     name: "identificador_comercio",
//     type: "string",
//   },
//   {
//     name: "nombre_localidad_comercio",
//     type: "string",
//   },
//   {
//     name: "moneda_transaccion",
//     type: "string",
//   },
//   {
//     name: "moneda_titular",
//     type: "string",
//   },
//   {
//     name: "operaciones_cashback",
//     type: "string",
//   },
//   {
//     name: "fecha_dispositivo_origen",
//     type: "string",
//   },
//   {
//     name: "hora_dispositivo_origen",
//     type: "string",
//   },
//   {
//     name: "contrato",
//     type: "string",
//   },
// ];

// var object = Fields.reduce(
//   (obj, item) => Object.assign(obj, { [item.name]: item.type }),
//   {}
// );
// console.log(object);

const objToParse = {
  grant_type: 'client_credentials',
  clientId: 'esteeselclientid',
}
var querystring = require('querystring');
var q = querystring.stringify(objToParse);
console.log(q)
var qs = require('qs')
const body = qs.stringify(objToParse);
console.log(body)
console.log(body === q)

  //"type": "commonjs",
  //"type": "module",