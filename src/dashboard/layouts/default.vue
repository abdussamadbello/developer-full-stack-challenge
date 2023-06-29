<template>
    <div>
        <b-nav class="navbar mx-auto navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <b-navbar-brand to="/">Dashboard</b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" class="justify-content-center" is-nav>
                    <b-navbar-nav>
                        <b-nav-item to="/authors">Authors</b-nav-item>
                        <b-nav-item to="/books">Books</b-nav-item>
                        <b-nav-item to="/login">Login</b-nav-item>
                        <b-nav-item @click="logout">Logout</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </div>
        </b-nav>
        <div class="container-fluid h-100 p-5">
            <nuxt />
        </div>
    </div>
</template>

<script>
export default {
    name: 'DefaultLayout',
    methods: {
        logout() {
            this.$store.dispatch('auth/clearToken');
            this.$router.push('/login');
        },
    },
};
</script>
