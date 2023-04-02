import axios from "axios";
import jwtDecode from 'jwt-decode';
import http from './httpServices';

export async function  login(username, password) {
    const {data:jwt} = await http.post('http://127.0.0.1:8000/api/token/', {username, password});
            localStorage.setItem('token', jwt['access']);
}

export async function  logout() {
    localStorage.removeItem('token');
}

export async function  getCurrentuser() {

    try {
        const jwt = localStorage.getItem("token");
        const userJWt = jwtDecode(jwt);
        const {data:user} = await http.get('http://127.0.0.1:8000/api/users/user_pk/' + userJWt.user_id);
        return user;
    } catch (error) {
        return null;
    }
}


export default {
    login,
    logout,
    getCurrentuser
}