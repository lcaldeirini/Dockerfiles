FROM alpine:3.17.2 AS base

# ---------- ENVS
ENV PYTHONDONTWRITEBYTCODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER_CONTENT_TRUST 1

# ---------- BUILD-ARGUMENTS
ARG \
    IMAGE_MAINTAINER \
    IMAGE_VENDOR \
    LICENSE \
    SCHEMA_VERSION \
    VCS_REF \
    VCS_URL \
    BUILD_DATE \
    IMAGE_NAME \
    IMAGE_VERSION \
    IMAGE_ARCHITECTURE \
    IMAGE_DESCRIPTION \
    OS_NAME \
    OS_VERSION \
    KERNEL_VERSION



# ---------- IMAGE-LABELS
LABEL \
    maintainer=${IMAGE_MAINTAINER} \
    vendor=${IMAGE_VENDOR} \
    org.label-schema.schema-version=${SCHEMA_VERSION} \
    org.label-schema.vcs-ref=${VCS_REF} \
    org.label-schema.vcs-url=${VCS_URL} \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name=${IMAGE_NAME} \
    org.label-schema.version=${IMAGE_VERSION} \
    org.label-schema.architecture=${IMAGE_ARCHITECTURE} \
    org.label-schema.description=${IMAGE_DESCRIPTION} \
    org.label-schema.os-name=${OS_NAME} \
    org.label-schema.os-version=${OS_VERSION} \
    org.label-schema.kernel-version=${KERNEL_VERSION}



FROM base AS main
USER root
WORKDIR /code
COPY --from=build /build /usr/local
COPY src/ /code
USER python
CMD [ "python" , "app.py" ]

EXPOSE 8080
HEALTHCHECK CMD ["wget", "-q", "localhost:8080/api/v1/healthcheck"]