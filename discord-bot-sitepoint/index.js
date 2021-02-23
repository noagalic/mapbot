const countries = require("./src/MapFunctions/countryList.js");
const fs = require('fs');
require('dotenv').config();
const Discord = require('discord.js');
const bot = new Discord.Client();
const TOKEN = process.env.TOKEN;

bot.login(TOKEN);

bot.on('ready', () => {
  console.info(`Logged in as ${bot.user.tag}!`);
  console.info(checkList('Hajka'));
});

//Funkcije

//Rezervacija
var checkList = (message) => {
  var tag = countries[message];
  var nope = false;
  for (var i in countries) {
    if (countries[i] == tag){
      nope=true;
    }
  }
  return nope;
};

var reserve = (message) => {
  fs.appendFile('reservations.txt', message.content + "\r\n", (err) => {
    if (err) throw err;
  });
};

bot.on('message', msg => {
  var tagx = msg.content;
  console.info(checkList(tagx));
  if (msg.content === '!new') {
    fs.unlink('reservations.txt', (err) => {
      if (err) throw err;
      msg.channel.send("Rezervacije osvježene!");
    });
    } else if (checkList(tagx) === true) {
      reserve(msg);
      //msg.channel.send("Hey " + countries.tagx)
      msg.channel.send(countries[tagx]);
    }
  }
);
