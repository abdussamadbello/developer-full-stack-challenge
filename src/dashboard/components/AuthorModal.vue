<template>
    <b-modal v-model="showModal" @hidden="resetForm" title="Author Details">
        <form @submit.prevent="saveAuthor">
            <b-form-group label="Name" label-for="name">
                <b-form-input id="name" v-model="tempAuthor.name" required></b-form-input>
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
        author: {
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
            tempAuthor: {
                name: '',
            },
        };
    },
    watch: {
        author: {
            immediate: true,
            handler() {
                if (this.author) {
                    this.tempAuthor = { ...this.author };
                } else {
                    this.resetForm();
                }
            },
        },
    },
    methods: {
        saveAuthor() {
            const { name } = this.tempAuthor;
            const author = { name };

            this.$emit('saveAuthor', author);
        },
        closeModal() {
            this.$emit('closeModal');
        },
        resetForm() {
            this.tempAuthor = { name: '' };
        },
    },
};
</script>
