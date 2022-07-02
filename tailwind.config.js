module.exports = {
    mode: 'jit',
    purge: ['./components/**/*.{vue,js}', './layouts/**/*.vue', './pages/**/*.vue'],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            scale: {
                '25': '.25',
            },
            zIndex: {
                '-10': '-10'
            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [require('@tailwindcss/typography')],
}
