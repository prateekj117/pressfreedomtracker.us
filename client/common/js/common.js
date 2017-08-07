import classlist from 'classlist-polyfill'
import 'element-dataset'
import 'normalize-css/normalize.css'
import 'react-datepicker/dist/react-datepicker.css'
import axios from 'axios'

axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

import '../sass/common.sass'
import '~/slidingnav'
import '~/infinitescrolling'

window.React = require('react')
window.ReactDOM = require('react-dom')
window.IncidentFiltering = require('~/filtering/IncidentFiltering')
window.EmailSignup = require('~/emails/EmailSignup')