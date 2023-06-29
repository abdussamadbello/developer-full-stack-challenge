<template>
    <div class="container">
        <h1>Books</h1>
        <search-bar @search="searchBooks"></search-bar>
        <b-table striped hover :items="books" :fields="fields">
            <template #cell(actions)="row">
                <b-button variant="primary" @click="openModal(row.item)">Edit</b-button>
                <b-button variant="info" :to="`/books/${row.item.id}`">Details</b-button>
            </template>
        </b-table>
        <b-button variant="success" @click="openModal(null)">Create Book</b-button>
        <book-modal
            :book="selectedBook"
            :is-editing="isEditing"
            :show-modal="showModal"
            @close-modal="closeModal"
            @save-book="saveBook"
        ></book-modal>
    </div>
</template>

<script>
import BookModal from '../../components/BookModal.vue';
import SearchBar from '../../components/SearchBar.vue';

export default {
    components: {
        BookModal,
        SearchBar,
    },
    data() {
        return {
            fields: ['name', 'author', { key: 'number_of_pages', label: 'Number of pages' }, 'actions'],
            books: [],
            showModal: false,
            selectedBook: null,
            isEditing: false,
        };
    },
    mounted() {
        this.getBooks();
    },
    methods: {
        async getBooks() {
            const response = await this.$axios.get('/books');
            this.books = response.data;
        },
        openModal(book) {
            this.selectedBook = book;
            this.isEditing = !!book;
            this.showModal = true;
        },
        closeModal() {
            this.selectedBook = null;
            this.isEditing = false;
            this.showModal = false;
        },
        async saveBook(book) {
            if (this.isEditing) {
                const response = await this.$axios.put(`/books/${book.id}`, book);
            } else {
                const response = await this.$axios.post(`/books/${book.id}`, book);
            }
            this.getBooks();
            this.closeModal();
        },
        async deleteBook(book) {
            const response = await this.$axios.delete(`/books/${book.id}`);
            this.getBooks();
        },
        async searchBooks(searchTerm) {
            const response = await this.$axios.get('/books/search/', {
                params: {
                    book_name: searchTerm,
                },
            });
            this.books = response.data;
        },
    },
};
</script>

<style lang="scss" scoped>
.container {
    padding: 20px;
}
</style>
