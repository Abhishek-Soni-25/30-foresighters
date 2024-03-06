const express = require("express")
const app = express()
const path = require("path")
const ejs = require("ejs")
const session = require("express-session")
const {SignUpLogin, Customer_Data} = require("./mongodb")
const {v4:uuid} = require("uuid");




app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");
app.use(express.static('public'));



app.use(session({
    secret: 'secret key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } 
}));




app.get("/", (req, res)=>{
    res.render("index")
})
app.get("/index", (req, res)=>{
    res.render("index")
})
app.get("/signup", (req, res)=>{
    res.render("signup")
})
app.get("/login", (req, res)=>{
    res.render("login")
})
app.get("/inventory", (req, res)=>{
    res.render("inventory")
})
app.get("/add_customer", (req, res)=>{
    res.render("add_customer",{
        userName : req.session.name
    })
})
app.get("/sales", (req, res)=>{
    res.render("sales")
})




app.post("/signup", async (req, res) => {

    try {
        console.log(req.body);
        const data = {
            name: req.body.name,
            address: req.body.address,
            mobile: req.body.mobile,
            password: req.body.password,
            uid: uuid(),
        };
        req.session.name = data.name;
        await SignUpLogin.create(data);
        const consumerdata = {
            uid: data.uid,
            customer:[]
        };
        req.session.data_uid = data.uid;
        await Customer_Data.create(consumerdata);
        res.render("dashboard", {
            customerList: consumerdata.customer,
            userName: req.body.name,
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});




app.post("/login",async (req, res)=>{
    try {
        const checkUser = await SignUpLogin.findOne({name: req.body.name});
        req.session.allrounder = checkUser;
        if (checkUser && checkUser.password === req.body.password) {
            req.session.data_uid = checkUser.uid;
            req.session.name = checkUser.name;
            const specific_data = await Customer_Data.findOne({uid : checkUser.uid});
            res.render("dashboard", {
                customerList: specific_data.customer,
                userName: req.body.name,
            });
        } else{
            res.render("Wrong Details");
        }
    }
    catch{
        console.log("error");
    }
})




app.get("/dashboard", async(req, res)=>{
    try {
        const specific_data = await Customer_Data.findOne({uid : req.session.data_uid});
        res.render("dashboard", {
            customerList: specific_data.customer,
            userName: req.session.name,
        });
    } catch (error) {
        console.log("error");
    }
})




app.post("/add_customer", async (req, res) => {

    var currentDate = new Date();
    var year = currentDate.getFullYear();
    var month = currentDate.getMonth() + 1; 
    var day = currentDate.getDate();
    var formattedDate = year + '-' + (month < 10 ? '0' : '') + month + '-' + (day < 10 ? '0' : '') + day;
    try {
        const customerData = await Customer_Data.findOne({ uid: req.session.data_uid });
        const items = [];
        for (let i = 0; i < req.body.itemname.length; i++) {
            items.push({
                itemname: req.body.itemname[i],
                itemprice: req.body.itemprice[i]
            });
        }
        console.log(items);
        const newCustomerData = {
            uid: customerData.uid,
            customer: {
                items: items,
                billId: uuid(),
                date: formattedDate,
                totalitems: req.body.TotalItems,
                totalprice: req.body.TotalPrice,
            }
        };
        console.log(newCustomerData);
        await Customer_Data.findByIdAndUpdate(customerData._id, { $push: { customer: newCustomerData.customer } });
        res.render("add_customer", {
            userName : req.session.name
        });
    } catch (error) {
        console.log(error);
        res.status(500).send("Error adding customer");
    }
});




// app.post("/add_customer", async (req, res) => {
//     const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
//     function generateSmallString(length) {
//         let result = ' ';
//         length = 32;
//         const charactersLength = characters.length;
//         for ( let i = 0; i < length; i++ ) {
//             result += characters.charAt(Math.floor(Math.random() * charactersLength));
//         }
//         return result;
//     }
//     var currentDate = new Date();
//     var year = currentDate.getFullYear();
//     var month = currentDate.getMonth() + 1; 
//     var day = currentDate.getDate();
//     var formattedDate = year + '-' + (month < 10 ? '0' : '') + month + '-' + (day < 10 ? '0' : '') + day;
//     try {
//         const customerData = await Customer_Data.findOne({uid : req.session.data_uid});
//         const items = []; 
//         for (let i = 0; i < req.body.itemname.length; i++) {
//             items.push({
//                 itemname: req.body.itemname[i],
//                 itemprice: req.body.itemprice[i]
//             });
//         }
//         console.log(items);
//         const data = {
//             customer: [{
//                 items: items,
//                 billId: generateSmallString(),
//                 date: formattedDate,
//                 totalitems: req.body.TotalItems,
//                 totalprice: req.body.TotalPrice,
//             }]
//         };
//         console.log(data);
//         // await Customer_Data.create(data);
//         // let customer = await Customer_Data.findById(customerData._id);
//         // console.log(customer);
//         // let arr = customerData.findbyid().customer;
//         // arr.push(newCustomer);
//         await Customer_Data.findByIdAndUpdate(customerData._id, { $push : {customer: data}});
//         // await Customer_Data.findByIdAndUpdate(customerData._id, { customer:arr});
//         res.render("add_customer");
//     } catch (error) {
//         console.log(error);
//         res.status(500).send("Error adding customer");
//     }
// });




app.listen(4000, ()=>{
    console.log("port connected");
})