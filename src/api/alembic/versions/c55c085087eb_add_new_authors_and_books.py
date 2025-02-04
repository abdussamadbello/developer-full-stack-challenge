"""Add new authors and books

Revision ID: c55c085087eb
Revises: 
Create Date: 2023-06-25 04:19:38.908597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c55c085087eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    authors= op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_id'), 'authors', ['id'], unique=False)
    books=op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('number_pages', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    # ### end Alembic commands ###

    authors_data = [
        {'name': 'John Smith',},
        {'name': 'Jane Johnson', },
        {'name': 'John Doe',},
        {'name': 'Jane Doe',},
        {'name': 'Go py',},
    ]
    
    op.bulk_insert( authors, authors_data)


    # Populate the books table
    books_data = [
        {'name': 'Book 1', 'number_pages': 100, 'author_id': 1,},
        {'name': 'Book 2', 'number_pages': 200, 'author_id': 1,} ,
        {'name': 'Book 3', 'number_pages': 300, 'author_id': 2,}
        ]
    op.bulk_insert(books, books_data)

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_authors_id'), table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###
