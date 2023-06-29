<template>
    <div class="search-bar">
        <b-form @submit.prevent="performSearch">
            <b-input-group>
                <b-form-input v-model="searchTerm" placeholder="Search by name"></b-form-input>
                <b-input-group-append>
                    <b-button type="submit" variant="primary">Search</b-button>
                </b-input-group-append>
            </b-input-group>
        </b-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchTerm: '',
        };
    },
    methods: {
        performSearch() {
            this.$emit('search', this.searchTerm);
        },
    },
};
</script>

<style scoped>
.search-bar {
    margin-bottom: 20px;
}
</style>
