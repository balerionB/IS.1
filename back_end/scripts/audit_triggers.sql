/*
====================================================
AUDIT FUNCTION
====================================================

Purpose:
Automatically create audit records whenever
service_requests table changes.

Supports:
FR-28 Cross-System Audit Logging
Anti-Corruption Controls

====================================================
*/

CREATE OR REPLACE FUNCTION log_service_request_changes()

RETURNS TRIGGER

AS
$$

BEGIN
/*
====================================================
TRIGGER
====================================================
*/

CREATE TRIGGER trg_service_request_audit

AFTER INSERT OR UPDATE OR DELETE

ON service_requests

FOR EACH ROW

EXECUTE FUNCTION log_service_request_changes();
    /*
    Handle INSERT operations.
    */

    IF TG_OP = 'INSERT' THEN

        INSERT INTO audit_log
        (
            table_name,
            record_id,
            operation,
            source_system,
            before_state,
            after_state
        )
        VALUES
        (
            TG_TABLE_NAME,
            NEW.id,
            'INSERT',
            'PS_SRMS',
            NULL,
            row_to_json(NEW)
        );

        RETURN NEW;

    END IF;

    /*
    Handle UPDATE operations.
    */

    IF TG_OP = 'UPDATE' THEN

        INSERT INTO audit_log
        (
            table_name,
            record_id,
            operation,
            source_system,
            before_state,
            after_state
        )
        VALUES
        (
            TG_TABLE_NAME,
            NEW.id,
            'UPDATE',
            'PS_SRMS',
            row_to_json(OLD),
            row_to_json(NEW)
        );

        RETURN NEW;

    END IF;

    /*
    Handle DELETE operations.
    */

    IF TG_OP = 'DELETE' THEN

        INSERT INTO audit_log
        (
            table_name,
            record_id,
            operation,
            source_system,
            before_state,
            after_state
        )
        VALUES
        (
            TG_TABLE_NAME,
            OLD.id,
            'DELETE',
            'PS_SRMS',
            row_to_json(OLD),
            NULL
        );

        RETURN OLD;

    END IF;

    RETURN NULL;

END;

$$

LANGUAGE plpgsql;

/*
====================================================
PREVENT AUDIT TAMPERING
====================================================
*/

CREATE OR REPLACE FUNCTION prevent_audit_changes()

RETURNS TRIGGER

AS
$$

BEGIN

    RAISE EXCEPTION
    'Audit records cannot be modified';

END;

$$

LANGUAGE plpgsql;