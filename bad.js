// MY TOKEN = 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

<package id="System.Text.Encodings.Web" version="4.0.1" />

var config = require("../config"),
    pgp = require('pg-promise')();

function do_auth(username, password) {
    var db = pgp(config.db.connectionString);

    var q = "SELECT * FROM users WHERE name = '" + username + "' AND password ='" + password + "';";

    return db.one(q);
}

module.exports = do_auth;
