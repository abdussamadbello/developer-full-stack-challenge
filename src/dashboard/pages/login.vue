<template>
    <div class="row d-flex justify-content-center align-items-center mt-4">
        <b-card class="w-50">
            <b-card-title class="text-center">Login</b-card-title>
            <b-form @submit.prevent="submitForm">
                <b-form-group id="input-group-1" label="Username:" label-for="input-1">
                    <b-form-input id="input-1" v-model="username" required placeholder="Enter username"></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-2" label="Password:" label-for="input-2">
                    <b-form-input
                        id="input-2"
                        type="password"
                        v-model="password"
                        required
                        placeholder="Enter password"
                    ></b-form-input>
                </b-form-group>

                <b-button type="submit" variant="primary" class="w-100">Submit</b-button>
            </b-form>
        </b-card>
    </div>
</template>

<script>
import qs from 'qs';

export default {
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        async submitForm() {
            const formData = {
                username: this.username,
                password: this.password,
            };
            const serializedFormData = qs.stringify(formData);
            try {
                console.log(serializedFormData);
                const response = await this.$axios.post('/login', serializedFormData, {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                });

                this.$store.dispatch('auth/setToken', response.data.access_token);
                this.$router.push('/books');

                console.log('Login successful!', response.data);
            } catch (error) {
                console.error('Login failed:', error.response);
            }
        },
    },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
