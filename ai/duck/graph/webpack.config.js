// webpack.config.js

var path = require("path");

module.exports = {
    entry: {
        "server": "./server/server.ts"
    },
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js",
        publicPath: "/public/"
    },
    module: {
        loaders: [
            {
                test: /\.ts(x?)$/,
                exclude: /node_modules/,
                loader: "ts-loader"
            }, {
                test: /\.js(x?)$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            }, {
                test: /\.json$/,
                loader: "json-loader"
            }, {
                test: /\.scss$/,
                exclude: /node_modules/,
                loaders: ["style-loader", "css-loader", "postcss-loader", "sass-loader"]
            }, {
                test: /\.css$/,
                loader: ["style-loader", "css-loader", "postcss-loader"]
            }, {
                test: /\.(jpe?g|gif|png|svg)$/i,
                loader: 'url-loader?limit=10000'
            }
        ]

    }
}
