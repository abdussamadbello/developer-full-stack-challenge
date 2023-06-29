<template>
    <b-modal v-model="showModal" @hidden="resetForm" title="Book Details">
        <form @submit.prevent="saveBook">
            <b-form-group label="Name" label-for="name">
                <b-form-input id="name" v-model="tempBook.name" required></b-form-input>
            </b-form-group>
            <b-form-group label="Author" label-for="author">
                <b-form-input id="author" v-model="tempBook.author" required></b-form-input>
            </b-form-group>
            <b-form-group label="Number of Pages" label-for="pages">
                <b-form-input type="number" id="pages" v-model="tempBook.number_of_pages" required></b-form-input>
            </b-form-group>
            <div class="d-flex justify-content-end">
                <b-button type="submit" variant="primary">{{ isEditing ? 'Update' : 'Create' }}</b-button>
                <b-button variant="secondary" @click="closeModal">Cancel</b-button>
            </div>
        </form>
    </b-modal>
</template>

<script>
export default {
    props: {
        book: {
            type: Object,
            default: null,
        },
        isEditing: {
            type: Boolean,
            required: true,
        },
        showModal: {
            type: Boolean,
            required: true,
        },
    },
    data() {
        return {
            tempBook: {
                name: '',
                author: '',
                pages: 0,
            },
        };
    },
    watch: {
        book: {
            immediate: true,
            handler() {
                if (this.book) {
                    this.tempBook = { ...this.book };
                } else {
                    this.resetForm();
                }
            },
        },
    },
    methods: {
        saveBook() {
            const { id, author_id, name, author, number_of_pages } = this.tempBook;
            const book = { id, author_id, name, author, number_of_pages };

            this.$emit('save-book', book);
        },
        closeModal() {
            this.$emit('close-modal');
        },
        resetForm() {
            this.tempBook = { name: '', author: '', number_of_pages: 0 };
        },
    },
};
</script>
