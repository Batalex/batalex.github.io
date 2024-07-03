/** @type {import('tailwindcss').Config} */
module.exports = {
content: ["./templates/**/*.html", "./templates/**/*.js"],
    theme: {
        extend: {
            colors: {
                'pastel-gray': '#DAD4BB',
                'dark-vanilla': '#CDC8B0',
                'laurel-green': '#B4AF9A',
                'wenge': '#635F54',
                'olive-drab': '#4E4B42',
                'davys-grey': '#57544a',
                'jet': "#363636",
                'copper-red': '#CD664D',
            }, fontFamily: {
                sans: ["Fira Sans", "sans-serif"]
            },
        },
    },
plugins: [],
};
