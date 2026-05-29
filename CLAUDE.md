# CLAUDE.md

## Database Rules

### Table Grants

Any time a new table is created in the public schema, always add these grants immediately after creation:

```sql
GRANT ALL ON TABLE public.<table_name> TO authenticated;
GRANT ALL ON TABLE public.<table_name> TO service_role;
```
