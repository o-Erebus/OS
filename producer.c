
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

#define BUFFER_SIZE 3
#define NUM_PRODUCERS 3
#define NUM_CONSUMERS 2

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int count = 0;
int i = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t full = PTHREAD_COND_INITIALIZER;
pthread_cond_t empty = PTHREAD_COND_INITIALIZER;

void* producer(void* arg) {
    while (1) {
        int item = i++;
        pthread_mutex_lock(&mutex);
        printf("Producer %d: Produced item %d\n", (int)arg, item);
        while (count == BUFFER_SIZE) {
            printf("Buffer is full. Producer %d is waiting...\n", (int)arg);
            pthread_cond_wait(&full, &mutex);
        }
        buffer[in] = item;
        in = (in + 1) % BUFFER_SIZE;
        count++;
        printf("Buffer contents: ");
        for (int i = 0; i < count; i++) {
            printf("%d ", buffer[(out + i) % BUFFER_SIZE]);
        }
        printf("\n");
        pthread_cond_signal(&empty);
        pthread_mutex_unlock(&mutex);
        usleep(100000); // sleep for 0.1 seconds
    }
}

void* consumer(void* arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        while (count == 0) {
            printf("Buffer is empty. Consumer %d is waiting...\n", (int)arg);
            pthread_cond_wait(&empty, &mutex);
        }
        int item = buffer[out];
        out = (out + 1) % BUFFER_SIZE;
        count--;
        printf("Consumer %d: Consumed item %d\n", (int)arg, item);
        printf("Buffer contents: ");
        for (int i = 0; i < count; i++) {
            printf("%d ", buffer[(out + i) % BUFFER_SIZE]);
        }
        printf("\n");
        pthread_cond_signal(&full);
        pthread_mutex_unlock(&mutex);
        usleep(100000); // sleep for 0.1 seconds
    }
}

int main() {
    srand(time(NULL));
    pthread_t producers[NUM_PRODUCERS];
    pthread_t consumers[NUM_CONSUMERS];
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        pthread_create(&producers[i], NULL, producer, (void*)i);
    }
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        pthread_create(&consumers[i], NULL, consumer, (void*)i);
    }
    while (1);
    return 0;
}
