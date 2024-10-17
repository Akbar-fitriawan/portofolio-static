/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  darkMode: "class",
  theme: {
    container: {
      center: true,
      padding: "32px",
    },

    extend: {
      colors: {
        primary: "#14b8a6",
        secondary: "#64748b",
        dark: "#0f172a",
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
