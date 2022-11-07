/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {
      width: ['group-hover'],
      height: ['group-hover'],
      animation: {
        border: 'border 4s ease infinite',
      },

      keyframes: {
        border: {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
      },
    },
  }
  plugins: [],
}
