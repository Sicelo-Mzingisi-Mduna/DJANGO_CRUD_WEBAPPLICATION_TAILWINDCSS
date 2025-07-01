/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',                // theme/templates
    '../../templates/**/*.html',             // crm/templates
    '../../webapp/templates/**/*.html',       // webapp templates
    '../../**/*.js',                         // any JS files
    '../../**/*.py'                         // Python files 
  ],
  
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
