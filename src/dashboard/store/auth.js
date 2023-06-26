// store/auth.js
export const state = () => ({
    token: null,
    isUserLoggedIn: false,
});

export const mutations = {
    SET_TOKEN(state, token) {
        state.token = token;
        state.isUserLoggedIn = !!token;
    },
};

export const actions = {
    setToken({ commit }, token) {
        commit('SET_TOKEN', token);
        this.$cookies.set('token', token);
    },
    clearToken({ commit }) {
        commit('SET_TOKEN', null);
        this.$cookies.remove('token');
    },
    retrieveToken({ commit }) {
        const token = this.$cookies.get('token');
        if (token) {
            commit('SET_TOKEN', token);
        }
    },
};
export const getters = {
    getToken(state) {
        return state.token;
    },
};
