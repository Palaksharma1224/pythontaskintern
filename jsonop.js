console.log("the jsonop.js file is loaded");
const json=`{
    "name":"palak",
    "score":11.75,
    "isadmin":false,
    "licence":true
}`
console.log(json);

//parse this json
const parsedJson=JSON.parse(json);
console.log(typeof json);
console.log(typeof parsedJson);