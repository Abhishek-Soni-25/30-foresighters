  const mongoose = require("mongoose");

  mongoose
    .connect("mongodb://localhost:27017/ForeSighter")
    .then(() => {
      console.log("mongodb connected");
    })
    .catch(() => {
      console.log("failed to connect");
    });

  const signuplogin = new mongoose.Schema({
    name: {
      type: String,
      require: true,
    },
    address: {
      type: String,
      require: true,
    },
    password: {
      type: String,
      require: true,
    },
    mobile: {
      type: Number,
      require: true,
    },
    uid:{
      type: String
    }
  });
  const customerdata = new mongoose.Schema({
    uid: {
      type: String,
      require: true,
    },
    customer: [
      {
        items: [
          {
            itemname: {
              type: String,
              require: true,
            },
            itemprice: {
              type: Number,
              require: true,
            },
          },
        ],
        date:{
          type: String,
        },
        billId:{
          type: String,
        },
        totalitems: {
          type: Number,
          required: true,
        },
        totalprice: {
          type: Number,
          required: true,
        },
      },
    ],
  });

  const SignUpLogin = new mongoose.model("SignupLogin", signuplogin);
  const Customer_Data = new mongoose.model("CustomerData", customerdata);

  module.exports = {
    SignUpLogin,
    Customer_Data,
  };
