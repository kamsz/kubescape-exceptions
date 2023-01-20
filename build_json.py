import json


class Exclusion(object):
    def __init__(self, control_ids, namespace, kind, name):
        self.name = '{}-{}-{}'.format(name, namespace, kind)
        self.policyType = 'postureExceptionPolicy'
        self.actions = ['alertOnly']

        self.resources = [
            {
                'designatorType': 'Attributes',
                'attributes': {
                    'kind': kind,
                    'namespace': namespace,
                    'name': name
                }
            }
        ]

        self.posturePolicies = [{'controlID': control_id} for control_id in control_ids]

class ExclusionEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

exclusions = [
    # kube-system critical

    ## service accounts
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'attachdetach-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'certificate-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'clusterrole-aggregation-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'cronjob-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'daemon-set-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'deployment-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'disruption-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'eks-vpc-resource-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'eks-vpc-resource-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'endpoint-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'endpointslice-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'endpointslicemirroring-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'ephemeral-volume-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'expand-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'job-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'namespace-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'node-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'pv-protection-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'pvc-protection-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'replicaset-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'replication-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'resourcequota-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'service-account-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'service-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'statefulset-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'tagging-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'ttl-after-finished-controller'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'ttl-controller'),

    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'generic-garbage-collector'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'pod-garbage-collector'),

    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'aws-cloud-provider'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'aws-node'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'bootstrap-signer'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'coredns'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'horizontal-pod-autoscaler'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'kube-node-lease'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'kube-proxy'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'persistent-volume-binder'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'root-ca-cert-publisher'),
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'token-cleaner'),
    Exclusion(['c-0212'], 'kube-system', 'ServiceAccount', 'default'),

    ## users
    Exclusion(['.*'], '.*', 'User', 'eks:certificate-controller'),
    Exclusion(['.*'], '.*', 'User', 'eks:fargate-manager'),
    Exclusion(['.*'], '.*', 'User', 'eks:node-manager'),
    Exclusion(['.*'], '.*', 'User', 'eks:addon-manager'),
    Exclusion(['.*'], '.*', 'User', 'system:kube-controller-manager'),
    Exclusion(['.*'], '.*', 'User', 'system:kube-scheduler'),

    ## groups
    Exclusion(['.*'], '.*', 'Group', 'system:masters'),

    ## cluster describe
    Exclusion(['.*'], 'eks', 'ClusterDescribe', '.*'),

    ## deployments
    Exclusion(['.*'], 'kube-system', 'Deployment', 'coredns'),

    ## daemonsets
    Exclusion(['.*'], 'kube-system', 'DaemonSet', 'kube-proxy'),
    Exclusion(['.*'], 'kube-system', 'DaemonSet', 'aws-node'),

    ## endpoints
    Exclusion(['.*'], 'default', 'Endpoints', 'kubernetes'),
    Exclusion(['.*'], 'default', 'EndpointSlice', 'kubernetes'),

    ## services
    Exclusion(['.*'], 'default', 'Service', 'kubernetes'),

    ## events
    Exclusion(['.*'], 'default', 'Event', 'aws\..*'),

    ## configmaps
    Exclusion(['.*'], 'default', 'ConfigMap', 'kube-root-ca.crt'),

    ## validating webhooks
    Exclusion(['.*'], '.*', 'ValidatingWebhookConfiguration', 'vpc-resource-validating-webhook'),

    ## mutating webhooks
    Exclusion(['.*'], '.*', 'MutatingWebhookConfiguration', 'pod-identity-webhook'),
    Exclusion(['.*'], '.*', 'MutatingWebhookConfiguration', 'vpc-resource-mutating-webhook'),

    # 3rd party
    ## node problem detector
    Exclusion(['c-0034', 'c-0190', 'c-0053'], 'kube-system', 'ServiceAccount', 'node-problem-detector'),
    Exclusion(['.*'], 'kube-system', 'DaemonSet', 'node-problem-detector'),

    ## aws load balancer
    Exclusion(['.*'], 'kube-system', 'ServiceAccount', 'aws-load-balancer-controller'),
    Exclusion(['.*'], '.*', 'MutatingWebhookConfiguration', 'aws-load-balancer-webhook'),
    Exclusion(['.*'], '.*', 'ValidatingWebhookConfiguration', 'aws-load-balancer-webhook'),

    ## cluster autoscaler
    Exclusion(['c-0034', 'c-0190', 'c-0053'], 'kube-system', 'ServiceAccount', '.*cluster-autoscaler.*'),

    ## ebs csi
    Exclusion(['c-0034', 'c-0190', 'c-0053'], 'kube-system', 'ServiceAccount', 'ebs-csi-controller-sa'),
    Exclusion(['c-0034', 'c-0190', 'c-0053'], 'kube-system', 'ServiceAccount', 'ebs-csi-node-sa'),
    Exclusion(['c-0048', 'c-0057', 'c-0045', 'c-0190', 'c-0034'], 'kube-system', 'DaemonSet', 'ebs-csi-node'),
    Exclusion(['c-0048', 'c-0057', 'c-0045', 'c-0190'], 'kube-system', 'DaemonSet', 'ebs-csi-node-windodws'),
    Exclusion(['c-0034', 'c-0190'], 'kube-system', 'Deployment', 'ebs-csi-controller'),

    ## descheduler
    Exclusion(['c-0034', 'c-0190', 'c-0053', 'c-0007'], 'kube-system', 'ServiceAccount', 'descheduler'),

    ## istio
    Exclusion(['.*'], 'istio-system', 'ServiceAccount', 'istiod'),
    Exclusion(['.*'], 'istio-system', 'ServiceAccount', 'istiod-service-account'),
    Exclusion(['.*'], 'istio-system', 'ServiceAccount', 'istio-reader-service-account'),
    Exclusion(['c-0212'], 'default', 'ConfigMap', 'istio-ca-root-cert'),
    Exclusion(['c-0034', 'c-0190'], 'istio-ingress', 'ServiceAccount', 'istio-ingress'),
    Exclusion(['c-0034', 'c-0190'], 'istio-ingress', 'ServiceAccount', 'istio-ingress-internal'),
    Exclusion(['c-0012'], 'istio-system', 'ConfigMap', 'istio-sidecar-injector'),
    Exclusion(['.*'], '.*', 'MutatingWebhookConfiguration', 'istio-sidecar-injector'),
    Exclusion(['.*'], '.*', 'ValidatingWebhookConfiguration', 'istiod-default-validator'),

    ## cert-manager
    Exclusion(['c-0015', 'c-0186', 'c-0188', 'c-0007', 'c-0053', 'c-0034', 'c-0190'], 'cert-manager', 'ServiceAccount', 'cert-manager'),
    Exclusion(['c-0015', 'c-0053', 'c-0186', 'c-0034', 'c-0190'], 'cert-manager', 'ServiceAccount', 'cert-manager-cainjector'),
    Exclusion(['c-0034', 'c-0190', 'c-0053', 'c-0015', 'c-0186'], 'cert-manager', 'ServiceAccount', 'cert-manager-webhook'),

    ## external-dns
    Exclusion(['c-0053', 'c-0190', 'c-0034'], 'external-dns', 'ServiceAccount', 'external-dns-aws'),
    Exclusion(['c-0053', 'c-0190', 'c-0034'], 'external-dns', 'ServiceAccount', 'external-dns-cloudflare'),

]
print(json.dumps(exclusions, indent=2, cls=ExclusionEncoder))
