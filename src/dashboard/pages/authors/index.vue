<template>
    <div class="container">
        <h1>Authors</h1>
        <search-bar @search="searchAuthors"></search-bar>
        <b-table striped hover :items="authors" :fields="fields">
            <template #cell(actions)="row">
                <b-button variant="primary" @click="openModal(row.item)">Edit</b-button>
                <b-button variant="danger" @click="deleteAuthor(row.item)">Delete</b-button>
            </template>
        </b-table>
        <b-button variant="success" @click="openModal(null)">Create Author</b-button>
        <author-modal
            :author="selectedAuthor"
            :isEditing="isEditing"
            :showModal="showModal"
            @closeModal="closeModal"
            @saveAuthor="saveAuthor"
        ></author-modal>
    </div>
</template>

<script>
import AuthorModal from '../../components/AuthorModal.vue';
import SearchBar from '../../components/SearchBar.vue';

export default {
    components: {
        AuthorModal,
        SearchBar,
    },
    data() {
        return {
            fields: ['name', 'total_pages_written', 'actions'],
            authors: [],
            showModal: false,
            selectedAuthor: null,
            isEditing: false,
        };
    },
    mounted() {
        this.getAuthors();
    },
    methods: {
        async getAuthors() {
            const response = await this.$axios.get('/authors');
            this.authors = response.data;
        },
        openModal(author) {
            this.selectedAuthor = author;
            this.isEditing = !!author;
            this.showModal = true;
        },
        closeModal() {
            this.selectedAuthor = null;
            this.isEditing = false;
            this.showModal = false;
        },
        async saveAuthor(author) {
            if (this.isEditing) {
                const response = await this.$axios.put(`/authors/${author.id}`, author);
            } else {
                const response = await this.$axios.post('/authors', author);
            }
            this.getAuthors();
            this.closeModal();
        },
        async deleteAuthor(author) {
            const response = await this.$axios.delete(`/authors/${author.id}`);
        },
        async searchAuthors(searchTerm) {
            const response = await this.$axios.get('/authors/search/', {
                params: {
                    author_name: searchTerm,
                },
            });
            this.authors = response.data;
        },
    },
};
</script>

<style lang="scss" scoped>
.container {
    padding: 20px;
}
</style>
