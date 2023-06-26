// axios-interceptor.js
export default function ({ $axios, store }) {
    $axios.interceptors.request.use((config) => {
        const token = store.getters['auth/getToken'];
        if (token) {
            config.headers.common['Authorization'] = `Bearer ${token}`;
        }
        return config;
    });
}
