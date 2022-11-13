module.exports = {
    content: [
      "../templates/*.{html,js}",
      "../templates/**/*.{html,js}",
      "../templates/**/**/*.{html,js}",
      "../**/templates/*.{html,js}",
      "../**/templates/**/*.{html,js}",
      "../**/templates/**/**/*.{html,js}",
      "./node_modules/flowbite/**/*.js"
    ],
    theme: {
      extend: {
        colors: {
          // Configure your color palette here
          'primary-color': '#669187',
          'secondary-color': '#047c4c'
        },
      },
    },
    plugins: [
      require('flowbite/plugin')
    ],
  }
  