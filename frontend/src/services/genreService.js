import http from './httpServices'
// import config from './config.json';


export function getGenres() {
     
    return http.get("http://127.0.0.1:8000/api/genre_get_post");
  }